n,m = map(int,input().split())
import sys
board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]

def searchAll():
    