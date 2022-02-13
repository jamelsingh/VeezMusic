# function to remove the downloaded files

import os

from pyrogram import Client, filters
from pyrogram.types import Message

from config import BOT_USERNAME
from helpers.decorators import errors, sudo_users_only
from helpers.filters import command


downloads = os.path.realpath("downloads")
raw = os.path.realpath("raw_files") # the code is not created for removing raw_files but if you want to create it, use this


@Client.on_message(command(["rmd", "clean", f"rmd@{BOT_USERNAME}", f"clean@{BOT_USERNAME}"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_downloads(_, message: Message):
    if ls_dir := os.listdir(downloads):
        for file in os.listdir(downloads):
            os.remove(os.path.join(downloads, file))
        await message.reply_text("✅ **removed all downloaded files**")
    else:
        await message.reply_text("❌ **no files is downloaded**")


@Client.on_message(command(["clear", f"clear@{BOT_USERNAME}"]) & ~filters.edited)
@errors
@sudo_users_only
async def clear_jpg_image(_, message: Message):
    pth = os.path.realpath(".")
    if ls_dir := os.listdir(pth):
        for dta in os.listdir(pth):
            os.system("rm -rf *.jpg")
        await message.reply_text("✅ **succesfully cleared**")
    else:
        await message.reply_text("✅ **already cleared**")
