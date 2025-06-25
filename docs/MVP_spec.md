# SimpleWMS MVP Specification

This document outlines the scope of the Minimal Viable Product (MVP) for the SimpleWMS project.

## Core Entities

The MVP includes the following key domain entities:

* **Article**: Identified by SKU, with attributes such as name, category (product, spare part, consumable), weight, volume, and optional expiration date.
* **Reception**: Logs incoming stock from a supplier, linking an article to an emplacement with a quantity and date.
* **Emplacement**: Represents physical locations (stock, sales floor, reservation, reception, expedition), with defined weight and volume capacities.
* **Implantation**: Defines the stock quantity and minimal threshold for an article in a specific emplacement.
* **Commande (Order)**: Contains multiple line items (article + quantity), and can be in various states (draft, reserved, prepared, shipped, cancelled).
* **Mission**: Represents a task related to stock operations such as move, inventory, reception, picking. Missions are assigned to agents and progress through defined statuses.
* **Agent**: A user or operator of the system.

## MVP Features

The MVP must support the following features:

### Article Management

* Add, edit, delete articles
* List/search articles

### Emplacement Management

* Create and manage emplacement zones with capacity definitions
* List all emplacements

### Reception Workflow

* Register receptions of articles from suppliers
* Link reception to emplacement

### Stock Implantation

* Define implantation of articles in emplacements with minimum threshold
* Display implantation per article or per emplacement

### Order Management

* Create orders with multiple articles and quantities
* Track order status (draft to shipped)

### Mission Handling

* Create missions for various operations: move, restock, inventory, reception, order preparation
* Assign missions to agents
* Track mission status (to-do, in progress, done, failed)

### Agent Management

* Add/edit/remove agents
* Activate/deactivate agent accounts

## Constraints

* All operations should be available via REST API endpoints
* The system will use a relational database for persistence

## Non-functional Requirements

* Code should be structured using FastAPI, SQLAlchemy and Alembic
* Follow RESTful best practices
* Use UUID as primary keys for all entities
