from selenium import webdriver
from selenium.webdriver.common.by import By
from playsound import playsound
import keyboard
import time

import discord
from discord.ext import commands, tasks
import asyncio

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://starrez.housing.gatech.edu/StarRezPortalX/EAB30B45/8/10/Home-My_Housing")

print("Login, go to the room selection page, and press F5 to start.")

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
  print("Bot is ready")
  
async def check_file():
  while True:
    if keyboard.is_pressed('f5'):
      while True:
        try:
          while True:
            await asyncio.sleep(5)
            try:
              before = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/section/form/div/div[1]/div[2]/ul[3]/li[2]/div").text
              a1 = before.splitlines()
            except:
              before = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/section/form/div/div[1]/div[2]/ul[1]/li[2]/div").text
              a1 = before.splitlines()
              pass
            driver.refresh()
            try:
              after = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/section/form/div/div[1]/div[2]/ul[3]/li[2]/div").text
              a2 = after.splitlines()
            except:
              after = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/section/form/div/div[1]/div[2]/ul[1]/li[2]/div").text
              a2 = before.splitlines()
              pass
            print(before + ",\n" + after + "\n-----\n")
            if not before == after:
              newbuildings = [elem for elem in a2 if elem not in a1]
              if not newbuildings: continue
              if not 'Smith' in newbuildings or not 'Harrison' in newbuildings or not 'Woodruff North' in newbuildings or not 'Woodruff South' in newbuildings:
                roomnumber = driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/section/form/div/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div/div/div/span/p/text()[1]")
                await client.get_channel(865381044327940128).send("*" + time.asctime(time.localtime(time.time())) + "*\n\nRooms now available in:\n**" + '\n'.join(newbuildings) + "** \n***First available room has automatically been added to cart. (" + roomnumber + ", 5 MINUTES)***\n-----")
                driver.find_element(By.XPATH, "/html/body/div[1]/section[1]/div/article/div/div/div/section/div[1]/section/form/div/div[2]/div[2]/div[1]/div[1]/div[3]/button[1]").click()
              else:
                await client.get_channel(865381044327940128).send("*" + time.asctime(time.localtime(time.time())) + "*\n\nRooms now available in:\n**" + '\n'.join(newbuildings) + "** \n-----")
              driver.switch_to.window(driver.current_window_handle)
              playsound("alert.mp3",0)
              print(time.asctime(time.localtime(time.time())) + ": Buildings have updated! " + ','.join(newbuildings))
        except Exception as e:
          print(e)
          pass


client.loop.create_task(check_file())
client.run("ODY1Mjc3NjkxMjg5MDEwMjA2.YPBqpQ.z8FCbUgrrg8JuN7XhubYxVT01y0")
