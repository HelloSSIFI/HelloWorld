import java.io.*;
import java.util.*;

class Main {
    static int n;
    static int[][][] quality;
    static char[][][] element;
    static boolean[] visited;
    static int answer;

    public static void rot(int[][] target) {                        // 입력받은 배열을 시계방향으로 90도 회전시키는 메소드
        int m = target.length;
        int[][] temp = new int[m][m];
        for (int r = 0; r < m; r++) {                               // 입력받은 배열을 복사
            for (int c = 0; c < m; c++) {
                temp[r][c] = target[r][c];
            }
        }
        for (int r = 0; r < m; r++) {                               // 90도 회전에 맞게 인덱스를 설정하여 값을 변경
            for (int c = 0; c < m; c++) {
                target[r][c] = temp[m - c - 1][r];
            }
        }
    }

    public static void rot(char[][] target) {                       // 타입이 다른 두 배열을 회전해야 하므로
        int m = target.length;                                      // 위 메소드와 같은 기능의 char 배열을 입력받는 메소드를 오버로딩
        char[][] temp = new char[m][m];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < m; c++) {
                temp[r][c] = target[r][c];
            }
        }
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < m; c++) {
                target[r][c] = temp[m - c - 1][r];
            }
        }
    }

    public static void dfs(int cnt, int[][] q, char[][] e) {
        if (cnt == 3) {                                                 // 3개의 재료를 골랐다면
            int score = 0;
            for (int r = 0; r < 5; r++) {                               // 점수 계산을 위해 만들어진 배열 순회
                for (int c = 0; c < 5; c++) {                           // 조건에 맞게 점수 합산 후
                    if (e[r][c] == 'R') {                               // 크다면 갱신해줌
                        score += 7 * q[r][c];
                    } else if (e[r][c] == 'B') {
                        score += 5 * q[r][c];
                    } else if (e[r][c] == 'G') {
                        score += 3 * q[r][c];
                    } else if (e[r][c] == 'Y') {
                        score += 2 * q[r][c];
                    }
                }
            }
            answer = Math.max(answer, score);
            return;
        }

        for (int k = 0; k < n; k++) {                                   // 순열을 만들어줌
            if (visited[k]) {                                           // 이미 고른 재료는 다시 고르지 않음
                continue;
            }
            visited[k] = true;                                          // 현재 고른 재료를 표시
            for (int l = 0; l < 4; l++) {                               // 4번 회전해야 하므로 4번 반복
                rot(quality[k]);                                        // 효능과 원소를 90도씩 회전
                rot(element[k]);
                for (int i = 0; i < 2; i++) {                           // 5 * 5 칸을 4 * 4 로 채워야 하므로
                    for (int j = 0; j < 2; j++) {                       // 재료의 왼쪽 위 좌표가 (0, 0) (0, 1) (1, 0) (1, 1) 4번 반복
                        int[][] newQ = new int[5][5];                   // 현재까지 만들어진 효능과 원소 배열을 복사
                        char[][] newE = new char[5][5];
                        for (int r = 0; r < 5; r++) {
                            for (int c = 0; c < 5; c++) {
                                newQ[r][c] = q[r][c];
                                newE[r][c] = e[r][c];
                            }
                        }
                        for (int r = 0; r < 4; r++) {                   // 문제 조건에 맞게 더해주고 색을 바꿔주고 재귀
                            for (int c = 0; c < 4; c++) {
                                newQ[r + i][c + j] = Math.max(Math.min(newQ[r + i][c + j] + quality[k][r][c], 9), 0);
                                if (element[k][r][c] == 'W') {
                                    continue;
                                }
                                newE[r + i][c + j] = element[k][r][c];
                            }
                        }
                        dfs(cnt + 1, newQ, newE);
                    }
                }
            }
            visited[k] = false;                                         // 현재 재료로 회전과 모든 위치에 재료넣기가 완료되면 고름 표시 제거
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        quality = new int[n][4][4];
        element = new char[n][4][4];
        visited = new boolean[n];
        int[][] initQ = new int[5][5];
        char[][] initE = new char[5][5];
        for (int r = 0; r < 5; r++) {
            for (int c = 0; c < 5; c++) {
                initE[r][c] = 'W';
            }
        }
        answer = 0;
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < 4; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 4; j++) {
                    quality[k][i][j] = Integer.parseInt(st.nextToken());
                }
            }
            for (int i = 0; i < 4; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 4; j++) {
                    element[k][i][j] = st.nextToken().charAt(0);                // 여기까지 입력받기 & 초기값 설정
                }
            }
        }
        dfs(0, initQ, initE);
        System.out.println(answer);
    }
}
