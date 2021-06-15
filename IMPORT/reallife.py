from django.contrib import admin
from django.urls import path
from django.conf.urls import  include ,url
import os
import sys
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Movie
from django.conf.urls import  include ,url
from rest_api import views  
from django.test import TestCase
from django.db import models
from django.apps import AppConfig
from django.contrib import admin
from rest_api.models import Movie
from django.core.wsgi import get_wsgi_application
from pathlib import Path
      

import flask
from flask import request, jsonify
from flask import Flask, render_template, url_for, request
import sqlite3 
from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import click
from flask import Flask
from flask.cli import AppGroup
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import DefaultMeta, Model
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from functools import wraps
from flask import g, request, redirect, url_for
