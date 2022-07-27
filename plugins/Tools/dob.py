import os
import pytz
import time
from random import choice
from shutil import rmtree
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
from pyrogram import Client, filters
from pyUltroid.functions.tools import async_searcher

@Client.on_message(filters.command("dob"))
async def dob(bot, message):
  
  match = message.text.split()
  
  if not match:
    return await message.reply("Provide your D.O.B. in XX/XX/XXXX format.")
  
  name = message.from_user.first_name
  k = await message.reply("Processing...")
  
  zn = pytz.timezone("Asia/Kolkata")
  abhi = dt.now(zn)
  p = match[1]
  r = match[2]
  s = match[3]
  print(p)
  print(r)
  print(s)
  day = int(p)
  month = r
  try:
      jn = dt.strptime(match, "%d/%m/%Y")  
  except BaseException:
      return await message.reply("something went wrong in line 34")
  jnm = zn.localize(jn)
  zinda = abhi - jnm
  barsh = (zinda.total_seconds()) / (365.242 * 24 * 3600)
  saal = int(barsh)
  mash = (barsh - saal) * 12
  mahina = int(mash)
  divas = (mash - mahina) * (365.242 / 12)
  din = int(divas)
  samay = (divas - din) * 24
  ghanta = int(samay)
  pehl = (samay - ghanta) * 60
  mi = int(pehl)
  sec = (pehl - mi) * 60
  slive = int(sec)
  y = int(s) + int(saal) + 1
  m = int(r)
  brth = dt(y, m, day)
  cm = dt(abhi.year, brth.month, brth.day)
  ish = (cm - abhi.today()).days + 1
  dan = ish
  if dan == 0:
      hp = "`Happy BirthDay To U🎉🎊`"
  elif dan < 0:
      okk = 365 + ish
      hp = f"{okk} Days Left 🥳"
  elif dan > 0:
      hp = f"{ish} Days Left 🥳"
  if month == "12":
      sign = "Sagittarius" if (day < 22) else "Capricorn"
  elif month == "01":
      sign = "Capricorn" if (day < 20) else "Aquarius"
  elif month == "02":
      sign = "Aquarius" if (day < 19) else "Pisces"
  elif month == "03":
      sign = "Pisces" if (day < 21) else "Aries"
  elif month == "04":
      sign = "Aries" if (day < 20) else "Taurus"
  elif month == "05":
      sign = "Taurus" if (day < 21) else "Gemini"
  elif month == "06":
      sign = "Gemini" if (day < 21) else "Cancer"
  elif month == "07":
      sign = "Cancer" if (day < 23) else "Leo"
  elif month == "08":
      sign = "Leo" if (day < 23) else "Virgo"
  elif month == "09":
      sign = "Virgo" if (day < 23) else "Libra"
  elif month == "10":
      sign = "Libra" if (day < 23) else "Scorpion"
  elif month == "11":
      sign = "Scorpio" if (day < 22) else "Sagittarius"
  json = await async_searcher(
      f"https://aztro.sameerkumar.website/?sign={sign}&day=today",
      post=True,
      re_json=True,
  )
  dd = json.get("current_date")
  ds = json.get("description")
  lt = json.get("lucky_time")
  md = json.get("mood")
  cl = json.get("color")
  ln = json.get("lucky_number")
    
  piza = f"""
Name -: {name}
D.O.B -:  {match}
Lived -:  {saal}yr, {mahina}m, {din}d, {ghanta}hr, {mi}min, {slive}sec
Birthday -: {hp}
Zodiac -: {sign}
**Horoscope On {dd} -**
`{ds}`
Lucky Time :-        {lt}
Lucky Number :-   {ln}
Lucky Color :-        {cl}
Mood :-                   {md}"""
    
  await k.edit(piza)
    
