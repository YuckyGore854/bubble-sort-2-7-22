import pygame
import random
import winsound

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Bubble sort")
running = True
width = 800/200
frequency = 37
duration = 20
def drawArr(arr):
    drawRect = pygame.Rect(0,0,800/200,0)
    for i in range(len(arr)):
        drawRect.x = i * width
        drawRect.y = 0
        drawRect.w = width
        drawRect.h = arr[i]
        
        pygame.draw.rect(screen, (255,255,255), drawRect)
nums = []

for i in range(200):
    nums.append(int(i))
drawArr(nums)
random.shuffle(nums)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            random.shuffle(nums)
    
    for i in range(len(nums)-1):
        screen.fill((0,0,0))
        drawArr(nums)
        
        if nums[i]>nums[i+1]:
            buffer = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = buffer
            frequency = i*30+37
            #winsound.Beep(frequency,duration)
            pygame.draw.rect(screen, (255,0,0), (i*width, 0, width, nums[i]))
        else:
            continue
        
    
        pygame.display.flip()


pygame.quit()