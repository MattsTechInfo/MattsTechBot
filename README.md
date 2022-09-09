# MattsTechBot
MattsTechBot is currently running in the MattsTechInfo Discord community server. It's nothing more than a copy of the work me (Matts) and Rutger have done on ClanBotJas for our gaming community. Since it's our own project, we've decided to keep developing on the original repo where this one is forked from. All updates to the original project will be synced to MattsTechBot to make it easy for community members to find and see the current running bot version in the community.

This Discord Bot, based on py-cord version 2.1.1, is a simple, self-hosted, custom bot to implement automatic Voice Channel scaling, self-role Text Channel administration, automatic roles on new member joins, polls and some basic command functions. It has been written to combat the woes of Voice Channel management (always having either too much or not enough Voice Channels) and Text Channel assignments for your Discord members. It also changes the name of a Voice Channel to the activity of connected users, automatically showing the topic of the Voice Channel. The self-role funtionality allows users to add roles to themselves so they can (un)subscribe Text Channels to/from their client using a dedicated configuration Text Channel.

## Automatic Builds
This project uses GitHub Actions to build and push new images to Docker Hub [clanbadjas/clanbotjas](https://hub.docker.com/r/clanbadjas/clanbotjas)

[![Docker Image CI](https://github.com/ClanBadJas/ClanBotJas/actions/workflows/docker-image.yml/badge.svg)](https://github.com/ClanBadJas/ClanBotJas/actions/workflows/docker-image.yml)

## Installation and configuration
MattsTechBot can be run as standalone Python application, as a pre-built container or as a container built from source.
Please see the [Wiki](https://github.com/ClanBadJas/ClanBotJas/wiki) for a full guide.
