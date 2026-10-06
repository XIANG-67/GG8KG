
def main():
    S = int(input())
    hours = S // 3600
   
    minutes = (S % 3600) // 60
    seconds = (S % 3600) % 60
    print(hours, minutes, seconds)
if __name__ == "__main__":
    main()