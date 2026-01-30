# Besita - Livestock Tracking System

A complete IoT-based livestock management and weight tracking system designed for livestock farms.

## Project Overview

**Besita** is an integrated system for monitoring and tracking livestock with automatic weight recording, health status management, and data analytics. The system consists of three main components:

- **ESP32 IoT Device**: Collects weight data from ADC sensors
- **Django Web Backend**: Manages animals, breeds, paddocks, and weight records
- **Data Processing**: Processes and visualizes livestock metrics

## System Architecture

```
┌─────────────────────────────────────────────────┐
│         Load Cell + ADS1232 ADC Sensor          │
└─────────────────────────────────────────────────┘
                        ↓
        ┌───────────────────────────────┐
        │      ESP32 Microcontroller    │
        │  - Data Collection            │
        │  - JSON Packaging             │
        │  - WiFi Communication         │
        └───────────────────────────────┘
                        ↓
        ┌───────────────────────────────┐
        │    Raspberry Pi               │
        │  - Data Relay                 │
        │  - Local Processing           │
        │  - Signal Processing          │
        │  - Local Database Storage     │
        │  - Cloud Data Sync            │
        └───────────────────────────────┘
                        ↓
        ┌───────────────────────────────┐
        │   Django Web Application      │
        │  - Database Management        │
        │  - Admin Panel                │
        │  - Analytics & Reports        │
        └───────────────────────────────┘
```

## Development Roadmap

- [x] Django models and database schema
- [x] Admin panel setup
- [ ] Complete Webpage Frontend
- [ ] REST API endpoints
- [ ] ESP32 firmware with ADC reading
- [ ] Signal Processing & Adaptive Filtering Algorithm
- [ ] Real-time sensor testing
- [ ] Raspberry Pi data relay implementation
- [ ] Cloud synchronization
- [ ] Mobile application
- [ ] Advanced analytics & reporting