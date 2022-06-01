n=int(input())
for row in range(0, n):
    stars_count = n - row
    left_stars = "* " * stars_count
    hollow_spaces = "  " * (2*row)
    right_stars = "* " * stars_count
    print(left_stars + hollow_spaces + right_stars)
for row in range(1, n+1):
    stars_count = n - row
    left_stars = "* " * row
    hollow_spaces = "  " * (2 * stars_count)
    right_stars = "* " * row
    print(left_stars + hollow_spaces + right_stars)      