package sample;

import java.util.Arrays;

class multAThread extends Thread {
    int[][] matrix;
    int[] array;
    int begin;
    int end;

    public multAThread(int[][] matrix, int[] array, int begin, int end) {
        this.matrix = matrix;
        this.array = array;
        this.begin = begin;
        this.end = end;
    }

    @Override
    public void run() {
        int m = matrix.length;
        int n = matrix[0].length;
        for (int i = begin; i < end; i++) {
            array[i] = 0;
            for (int k = 0; k < n - n%2; k += 2)
                array[i] -= matrix[i][k] * matrix[i][k + 1];
        }
        super.run();
    }
}

class multBThread extends Thread {
    int[][] matrix;
    int[] array;
    int begin;
    int end;

    public multBThread(int[][] matrix, int[] array, int begin, int end) {
        this.matrix = matrix;
        this.array = array;
        this.begin = begin;
        this.end = end;
    }

    @Override
    public void run() {
        int q = matrix[0].length;
        int n = matrix.length;
        for (int i = begin; i < end; i++) {
            array[i] = 0;
            for (int k = 0; k < n - n%2; k += 2)
                array[i] -= matrix[k][i] * matrix[k + 1][i];
        }
        super.run();
    }
}

class winoThread extends Thread {
    int[][] a;
    int[][] b;
    int[][] c;
    int[] multA;
    int[] multB;
    int begin;
    int end;

    public winoThread(int[][] a, int[][] b, int[][] c, int[] multA, int[] multB, int begin, int end) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.multA = multA;
        this.multB = multB;
        this.begin = begin;
        this.end = end;
    }

    @Override
    public void run() {
        int m = a.length;
        int n = b.length;
        int q = b[0].length;

        for (int i = begin; i < end; i++)
            for (int j = 0; j < q; j++) {
                c[i][j] = multA[i] + multB[j];
                for (int k = 0; k < n - n%2; k += 2)
                    c[i][j] += (a[i][k] + b[k+1][j]) * (a[i][k+1] + b[k][j]);
                if (n%2 == 1)
                    c[i][j] += a[i][n-1] * b[n-1][j];
            }
        super.run();
    }
}


public class Main {
    public static void singleWinograd(int[][] a, int[][] b, int[][] c) {
        int m = a.length;
        int n = b.length;
        int q = b[0].length;

        int[] multA = new int[m];
        for (int i = 0; i < m; i++) {
            multA[i] = 0;
            for (int k = 0; k < n - n%2; k += 2)
                multA[i] -= a[i][k] * a[i][k + 1];
        }

        int[] multB = new int[q];
        for (int i = 0; i < q; i++) {
            multB[i] = 0;
            for (int k = 0; k < n - n%2; k += 2)
                multB[i] -= b[k][i] * b[k + 1][i];
        }

        for (int i = 0; i < m; i++)
            for (int j = 0; j < q; j++) {
                c[i][j] = multA[i] + multB[j];
                for (int k = 0; k < n - n%2; k += 2)
                    c[i][j] += (a[i][k] + b[k+1][j]) * (a[i][k+1] + b[k][j]);
                if (n % 2 == 1)
                    c[i][j] += a[i][n-1] * b[n-1][j];
            }
    }

    public static void multiWinograd(int[][] a, int[][] b, int[][] c, int numThreads) throws InterruptedException {    //все потоки на mult и потом на умножении
        int m = a.length;
        int n = b.length;
        int q = b[0].length;

        int[] multA = new int[m];
        int[] multB = new int[q];
        Thread[] threads = new Thread[numThreads];
        int threadsInUse = 0;

        int rowsPerThread = m / numThreads;
        if (rowsPerThread == 0)
            rowsPerThread = 1;

        for (int i = 0, row = 0; i < numThreads && row < m; i++, row += rowsPerThread) {
            if (i+1 != numThreads)
                threads[i] = new multAThread(a, multA, row, row + rowsPerThread);
            else
                threads[i] = new multAThread(a, multA, row, m);
            threadsInUse++;
        }

        for (int i = 0; i < threadsInUse; i++)
            threads[i].start();

        for (int i = 0; i < threadsInUse; i++)
            threads[i].join();

        threadsInUse = 0;

        int colsPerThread = q / numThreads;
        if (colsPerThread == 0)
            colsPerThread = 1;

        for (int i = 0, col = 0; i < numThreads && col < q; i++, col += colsPerThread) {
            if (i+1 != numThreads)
                threads[i] = new multBThread(b, multB, col, col + colsPerThread);
            else
                threads[i] = new multBThread(b, multB, col, q);
            threadsInUse++;
        }

        for (int i = 0; i < threadsInUse; i++)
            threads[i].start();

        for (int i = 0; i < threadsInUse; i++)
            threads[i].join();

        threadsInUse = 0;
        rowsPerThread = m / numThreads;
        if (rowsPerThread == 0)
            rowsPerThread = 1;
        for (int i = 0, row = 0; i < numThreads && row < m; i++, row += rowsPerThread) {
            if (i+1 != numThreads)
                threads[i] = new winoThread(a, b, c, multA, multB, row, row + rowsPerThread);
            else
                threads[i] = new winoThread(a, b, c, multA, multB, row, m);
            threadsInUse++;
        }
        for (int i = 0; i < threadsInUse; i++)
            threads[i].start();

        for (int i = 0; i < threadsInUse; i++)
            threads[i].join();
    }

    public static void multiWinograd2(int[][] a, int[][] b, int[][] c, int numThreads) throws InterruptedException { // mult однопоток, умн - все
        int m = a.length;
        int n = b.length;
        int q = b[0].length;

        int[] multA = new int[m];
        for (int i = 0; i < m; i++) {
            multA[i] = 0;
            for (int k = 0; k < n - n%2; k += 2)
                multA[i] -= a[i][k] * a[i][k + 1];
        }

        int[] multB = new int[q];
        for (int i = 0; i < q; i++) {
            multB[i] = 0;
            for (int k = 0; k < n - n%2; k += 2)
                multB[i] -= b[k][i] * b[k + 1][i];
        }

        Thread[] threads = new Thread[numThreads];
        int threadsInUse = 0;

        int rowsPerThread = m / numThreads;
        if (rowsPerThread == 0)
            rowsPerThread = 1;
        for (int i = 0, row = 0; i < numThreads && row < m; i++, row += rowsPerThread) {
            if (i+1 != numThreads)
                threads[i] = new winoThread(a, b, c, multA, multB, row, row + rowsPerThread);
            else
                threads[i] = new winoThread(a, b, c, multA, multB, row, m);
            threadsInUse++;
        }

        for (int i = 0; i < threadsInUse; i++)
            threads[i].start();

        for (int i = 0; i < threadsInUse; i++)
            threads[i].join();
    }

    public static void main(String[] args) throws InterruptedException {
        int[][] a = {{3, 7, -2, 0}, {-11, 7, 3, 1}};
        int[][] b = {{1, 0, 11}, {-1,  7, 17}, {2, 6, -14}, {-3, -4, -22}};
        int[][] c = {{0, 0, 0}, {0, 0, 0}};

        singleWinograd(a, b, c);
        System.out.println(Arrays.deepToString(c));
        c = new int[][]{{0, 0, 0}, {0, 0, 0}};
        multiWinograd(a, b, c, 2);
        System.out.println(Arrays.deepToString(c));
        c = new int[][]{{0, 0, 0}, {0, 0, 0}};
        multiWinograd2(a, b, c, 2);
        System.out.println(Arrays.deepToString(c));

//        Testing.test();
//        analysis(500, 8);
    }

    public static void analysis(int size, int realThreads) throws InterruptedException {
        int[][] a = new int[size][size];
        int[][] b = new int[size][size];
        int[][] c = new int[size][size];

        for (int i = 0; i < size; i++)
            for (int j = 0; j < size; j++) {
                a[i][j] = i;
                b[i][j] = j;
                c[i][j] = 0;
            }

        long begin, end, s = 0;
        for (int k = 0; k < 10; k++) {
            begin = System.nanoTime();
            singleWinograd(a, b, c);
            end = System.nanoTime();
            s += end-begin;
            for (int i = 0; i < size; i++)
                for (int j = 0; j < size; j++)
                    c[i][j] = 0;
        }
        System.out.println("Single-thread version: " + s / 10_000_000.0);

        System.out.println("Multi-thread version 1");
        for (int t = 1; t < realThreads * 4 + 1; t *= 2) {
            s = 0;
            for (int k = 0; k < 10; k++) {
                begin = System.nanoTime();
                multiWinograd(a, b, c, t);
                end = System.nanoTime();
                s += end-begin;
                for (int i = 0; i < size; i++)
                    for (int j = 0; j < size; j++)
                        c[i][j] = 0;
            }
            System.out.println(t + ": " + s / 10_000_000.0);
        }

        System.out.println("Multi-thread version 2");
        for (int t = 1; t < realThreads * 4 + 1; t *= 2) {
            s = 0;
            for (int k = 0; k < 10; k++) {
                begin = System.nanoTime();
                multiWinograd2(a, b, c, t);
                end = System.nanoTime();
                s += end-begin;
                for (int i = 0; i < size; i++)
                    for (int j = 0; j < size; j++)
                        c[i][j] = 0;
            }
            System.out.println(t + ": " + s / 10_000_000.0);
        }
    }
}

class Testing {
    public static void test() {
        test_single();
        test_multi1();
        test_multi2();
    }

    private static void test_single() {
        System.out.println("Тестирование одногопоточного алгоритма");

        int[][] a = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        int[][] b = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        int[][] c = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int[][] res = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

        Main.singleWinograd(a, b, c);
        System.out.print("Единичные матрицы: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{1, 2, 3}, {3, 2, 1}, {2, 3, 1}};
        b = new int[][] {{1, 1, 1}, {2, 2, 2}, {3, 3, 3}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{14, 14, 14}, {10, 10, 10}, {11, 11, 11}};

        Main.singleWinograd(a, b, c);
        System.out.print("Квадратные матрицы: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{3, 7, -2}, {-11, 7, 3}};
        b = new int[][] {{1, 0, 11}, {-1,  7, 17}, {2, 6, -14}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{-8, 37, 180}, {-12, 67, -44}};

        Main.singleWinograd(a, b, c);
        System.out.print("Прямоугольные матрицы нечет.: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{3, 7, -2, 0}, {-11, 7, 3, 1}};
        b = new int[][] {{1, 0, 11}, {-1,  7, 17}, {2, 6, -14}, {-3, -4, -22}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{-8, 37, 180}, {-15, 63, -66}};

        Main.singleWinograd(a, b, c);
        System.out.print("Прямоугольные матрицы чет.: ");
        System.out.println(Arrays.deepEquals(c, res));
    }

    private static void test_multi1() {
        System.out.println("Тестирование многопоточного алгоритма 1");

        int[][] a = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        int[][] b = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        int[][] c = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int[][] res = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

        try { Main.multiWinograd(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Единичные матрицы: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{1, 2, 3}, {3, 2, 1}, {2, 3, 1}};
        b = new int[][] {{1, 1, 1}, {2, 2, 2}, {3, 3, 3}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{14, 14, 14}, {10, 10, 10}, {11, 11, 11}};

        try { Main.multiWinograd(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Квадратные матрицы: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{3, 7, -2}, {-11, 7, 3}};
        b = new int[][] {{1, 0, 11}, {-1,  7, 17}, {2, 6, -14}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{-8, 37, 180}, {-12, 67, -44}};

        try { Main.multiWinograd(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Прямоугольные матрицы нечет.: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{3, 7, -2, 0}, {-11, 7, 3, 1}};
        b = new int[][] {{1, 0, 11}, {-1,  7, 17}, {2, 6, -14}, {-3, -4, -22}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{-8, 37, 180}, {-15, 63, -66}};

        try { Main.multiWinograd(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Прямоугольные матрицы чет.: ");
        System.out.println(Arrays.deepEquals(c, res));
    }

    private static void test_multi2() {
        System.out.println("Тестирование многопоточного алгоритма 2");

        int[][] a = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        int[][] b = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};
        int[][] c = {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        int[][] res = {{1, 0, 0}, {0, 1, 0}, {0, 0, 1}};

        try { Main.multiWinograd2(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Единичные матрицы: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{1, 2, 3}, {3, 2, 1}, {2, 3, 1}};
        b = new int[][] {{1, 1, 1}, {2, 2, 2}, {3, 3, 3}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{14, 14, 14}, {10, 10, 10}, {11, 11, 11}};

        try { Main.multiWinograd2(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Квадратные матрицы: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{3, 7, -2}, {-11, 7, 3}};
        b = new int[][] {{1, 0, 11}, {-1,  7, 17}, {2, 6, -14}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{-8, 37, 180}, {-12, 67, -44}};

        try { Main.multiWinograd2(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Прямоугольные матрицы нечет.: ");
        System.out.println(Arrays.deepEquals(c, res));

        a = new int[][] {{3, 7, -2, 0}, {-11, 7, 3, 1}};
        b = new int[][] {{1, 0, 11}, {-1,  7, 17}, {2, 6, -14}, {-3, -4, -22}};
        c = new int[][] {{0, 0, 0}, {0, 0, 0}};
        res = new int[][] {{-8, 37, 180}, {-15, 63, -66}};

        try { Main.multiWinograd2(a, b, c, 8); } catch (InterruptedException e) { e.printStackTrace(); }
        System.out.print("Прямоугольные матрицы чет.: ");
        System.out.println(Arrays.deepEquals(c, res));
    }
}
