# 🚦 YOLOv8 Traffic Vehicle Detection System

> Real-time detection and tracking of traffic vehicles using YOLOv8

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![YOLO](https://img.shields.io/badge/YOLOv8-Ultralytics-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/sybink/your-repo-name)

## 📋 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Vehicle Classes](#-vehicle-classes)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
  - [Training](#training)
  - [Detection](#detection)
  - [Tracking](#tracking)
- [Results](#-results)
- [Video Demo](#-video-demo)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🎯 Overview

This project implements **YOLOv8** for detecting and tracking vehicles in traffic scenes. The system is specifically trained on Vietnamese traffic conditions and can identify four types of vehicles commonly seen on Vietnamese roads.

## ✨ Features

- ✅ **4-Class Vehicle Detection** - Bus, Car, Motorbike, Truck
- ✅ **Real-time Tracking** - Object tracking with `main_tracking.py`
- ✅ **Vietnamese Traffic Optimized** - Trained on local traffic data
- ✅ **Multiple Input Formats** - Images, Videos, YouTube links
- ✅ **Easy to Use** - Simple scripts for training and inference
- ✅ **GPU Acceleration** - CUDA support for fast processing

## 🚗 Vehicle Classes

| Class ID | Vehicle Type | Vietnamese | Description |
|----------|--------------|------------|-------------|
| 0 | 🚌 **Bus** | Xe buýt | Public transportation buses |
| 1 | 🚗 **Car** | Xe ô tô | Private cars and sedans |
| 2 | 🏍️ **Motorbike** | Xe máy | Motorcycles and scooters |
| 3 | 🚚 **Truck** | Xe tải | Cargo and delivery trucks |

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| Python | 3.10+ | Programming language |
| Ultralytics YOLO | 8.0+ | Object detection framework |
| PyTorch | 2.0+ | Deep Learning |
| OpenCV | 4.8+ | Image/Video processing |
| NumPy | 1.24+ | Numerical computing |

## 📁 Project Structure
