from typing import List, Tuple

def linear_search(arr: List[int], target: int) -> Tuple[int, int]:
    comparisons = 0
    for i, value in enumerate(arr, start=1):
        comparisons += 1
        if value == target:
            return i, comparisons
    return -1, comparisons

def binary_search(arr: List[int], target: int) -> Tuple[int, int]:
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid + 1, comparisons
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, comparisons

def main():
    student_ids = [1001, 1005, 1002, 1008, 1003, 1010, 1004, 1009, 1007, 1012,
                   1015, 1006, 1011, 1013, 1014, 1016, 1017, 1018, 1019, 1020]

    sorted_scores = [45, 52, 58, 63, 67, 72, 75, 78, 82, 85,
                     88, 90, 92, 95, 98, 99, 100, 104, 106, 110]

    print("\n=== Searching Algorithms Menu ===")

    while True:
        print("""
Select a search operation (1-3):
1. Linear Search - Find Student ID
2. Binary Search - Find Score
3. Exit program
""")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print(f"Searching in the list: {student_ids}")
            target = int(input("Enter Student ID to search: "))
            pos, comp = linear_search(student_ids, target)
            if pos != -1:
                print(f"Result: Student ID {target} found at position {pos} Comparisons made: {comp}")
            else:
                print(f"Result: Student ID {target} NOT found Comparisons made: {comp}")

        elif choice == "2":
            print(f"Sorted scores: {sorted_scores}")
            target = int(input("Enter score to search: "))
            pos, comp = binary_search(sorted_scores, target)
            if pos != -1:
                print(f"Result: Score {target} found at position {pos} Comparisons made: {comp}")
            else:
                print(f"Result: Score {target} NOT found Comparisons made: {comp}")

        elif choice == "3":
            print("\nThank you for using the search program!")
            break

        else:
            print("Invalid choice! Try again.")
            continue

        again = input("Would you like to perform another search? (y/n): ").lower()
        if again != "y":
            print("\nThank you for using the search program!")
            break

if __name__ == "__main__":
    main()
