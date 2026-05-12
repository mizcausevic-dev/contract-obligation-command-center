# Architecture

## Goal

Represent a legal-ops command layer that helps teams see which agreement needs intervention first, why it is at risk, and which owner lane must move next.

## Core model

- `agreements`
  - agreement type
  - renewal date
  - owner lane
  - obligation window
  - approval blocker
  - commercial exposure
- `obligations`
  - title
  - severity
  - owner
  - deadline pressure
  - recommended action

## Service behavior

`ContractService` loads sample contract data and decorates each agreement with a normalized queue lane:

- `escalate`
  - near-term deadline or severe contractual pressure
- `watch`
  - material blocker inside the next review cycle
- `clear`
  - low-pressure agreements that only need cadence tracking

## Experience surfaces

- `/`
  - executive overview
- `/queue`
  - agreement-level priority queue
- `/obligations`
  - obligation board by severity and owner
- `/api-summary`
  - sample downstream integration payload

## Why this repo is useful

This repo is intentionally operational rather than generative. It does not attempt contract drafting or legal advice. Instead, it focuses on obligation visibility, ownership gaps, renewal pressure, and the workflow mechanics that determine whether contractual risk stays contained.
