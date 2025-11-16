from typing import List, Tuple

def bubble_sort(names: List[str]) -> List[str]:
    arr = names[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j].lower() > arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(scores: List[int]) -> List[int]:
    arr = scores[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def quick_sort(prices: List[int]) -> Tuple[List[int], int]:
    calls = 0
    def qs(arr):
        nonlocal calls
        calls += 1
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return qs(left) + mid + qs(right)

    return qs(prices[:]), calls


NAMES = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "Choki", "Sonam",
         "Jigme", "Pema", "Thinley", "Kinley", "Tashi", "Ugyen", "Dechen", "Wangmo"]

SCORES = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59,
          76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

PRICES = [450, 230, 678, 125, 890, 320, 510, 275, 640,
          150, 720, 305, 480, 560, 410]


def main():

    print("\n=== Sorting Algorithms Menu ===")

    while True:
        print("""
Select a sorting operation (1-4):
1. Bubble Sort - Sort Student Names
2. Insertion Sort - Sort Test Scores
3. Quick Sort - Sort Book Prices
4. Exit program
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            print(f"Original names: {NAMES}")
            sorted_list = bubble_sort(NAMES)
            print(f"Sorted names:   {sorted_list}")

        elif choice == "2":
            print(f"Original scores: {SCORES}")
            sorted_scores = insertion_sort(SCORES)
            print(f"Sorted scores:   {sorted_scores}")
            print("\nTop 5 Scores:")
            for i, s in enumerate(sorted_scores[-1:-6:-1], start=1):
                print(f"{i}. {s}")

        elif choice == "3":
            print(f"Original prices: {PRICES}")
            sorted_prices, calls = quick_sort(PRICES)
            print(f"Sorted prices:   {sorted_prices}")
            print(f"Recursive calls: {calls}")

        elif choice == "4":
            print("\nThank you for using the sorting program!")
            break

        else:
            print("Invalid choice! Try again.")
            continue

        again = input("Would you like to perform another sort? (y/n): ").lower()
        if again != "y":
            print("\nThank you for using the sorting program!")
            break


if __name__ == "__main__":
    main()
