# git add .; git commit; git push;
'''
We have a water company that delivers water to landscaping companies in 
the metro Atlanta area. The have recently salvage some materials from a 
scrap yard to wield together to make their first water tank to help 
transport their mineral water to the landscaping companies sites.

Give this array of material heights (index value) and the possible width 
of the container (the distance between each indexes). We want to 
calculate the largest container configuration.

Notes
- I currently know the heights of each material
- I know that the materials aren't able to be reshuffled and has to stay 
in place of the array
- each pointer has to be able to calculate the width, height, and the 
surface area before determining the best config
- return the maximum amount of water that the container can hold length x 
width
- pointers have to keep the height of the container
- need a vary to log the maximum water capacity
'''

heights = [1, 8, 6, 9, 5, 4, 8, 3, 7]

def calc_water_capacity(heights_arr):
    left = 0
    right = len(heights_arr) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(heights_arr[left], heights_arr[right])
        current_water = width * current_height

        max_water = max(max_water, current_water)

        if heights_arr[left] < heights_arr[right]:
            left += 1
        else:
            right -= 1

    return max_water

result = calc_water_capacity(heights)
print(f"Maximum water capacity: {result}")