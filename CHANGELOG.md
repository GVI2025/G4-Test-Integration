# [1.0.0] (2025-06-18)

### Added

- **Room Management**: Add, edit, delete, and list/search rooms.
- **Reservation Management**: Create and list reservations associated to user ids and rooms.
- REST API endpoints for all core entities and workflows.
- Database schema and migrations using Alembic.
- Initial data seeding script for testing purposes.
- FastAPI-based application with Swagger UI for API documentation.

# [1.1.0] (2025-06-22)

### Added

- `disponible` parameter updated with a scheduler, allowing users to filter rooms based on availability.
- filtering by room availability in the list of rooms.
- Added deletion of reservations.
- Added `commentaire` field to reservations.
