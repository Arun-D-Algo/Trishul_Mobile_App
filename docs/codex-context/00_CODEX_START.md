# TRISHUL 2.0 — Codex Context Pack

## Purpose
This repository is the implementation context for SIH26192, a software prototype for flash-flood prediction and evacuation support in hilly regions.

## Primary instruction to Codex
Build a working, demoable, modular prototype. Prefer a vertical slice that actually runs over speculative infrastructure.

## Product
**TRISHUL 2.0 — AI Flash Flood Prediction & Network-Resilient Evacuation Platform**

## Problem
Ministry of Home Affairs, SIH26192, Disaster Management. Primary users are District Disaster Management Authorities, search and rescue teams, residents of hilly regions, and trekkers/tourists.

## Core promise
Fuse weather, terrain, local observations and citizen reports into localized flood-risk assessment and actionable evacuation guidance, including operation when connectivity is unreliable.

## MVP truth
The one-week prototype must reliably demonstrate:
1. deterministic scenario/weather inputs
2. localized risk assessment
3. terrain/elevation context
4. estimated hazard arrival vs evacuation time
5. dynamic route changes when a road/bridge is unsafe
6. citizen report/SOS
7. command dashboard
8. offline/demo operation

## Architecture
Use a modular monolith backend with Flutter mobile and a web dashboard. External providers are adapters. Heavy GIS processing is precomputed. Real BLE, acoustic, CCTV/YOLO, barometer and satellite processing are optional extensions.

## Important correction to the original concept
Atmospheric pressure changes are auxiliary only and must not be presented as a primary flash-flood predictor. Do not claim universal 15-minute prediction. Use `localized risk assessment` and `estimated hazard arrival`.

## Context hierarchy
For execution, follow `AGENTS.md`, then `docs/CODEX_BUILD_PLAN.md`, then `docs/TEAM_SPLIT.md`, then this context pack.
