# ALX Travel App

A Django-based travel booking application that allows users to browse listings, make bookings, and leave reviews for properties.

## 📁 Project Structure

```
alx_travel_app/
├── .env                        # Environment variables (SECRET_KEY, DATABASE_URL, etc.)
├── .gitignore                  # Git ignore file
├── database_setup.sql          # Database initialization script
├── manage.py                   # Django management script
├── README.md                   # Project documentation
├── alx_travel_app/            # Main Django project directory
│   ├── __init__.py
│   ├── asgi.py                # ASGI configuration for deployment
│   ├── requirement.txt        # Python dependencies
│   ├── settings.py            # Django settings configuration
│   ├── urls.py                # Main URL routing
│   └── wsgi.py                # WSGI configuration for deployment
├── listings/                  # Django app for property listings
│   ├── __init__.py
│   ├── admin.py               # Django admin configuration
│   ├── apps.py                # App configuration
│   ├── models.py              # Database models (Listing, Booking, Review)
│   ├── serializers.py         # DRF serializers for API endpoints
│   ├── tests.py               # Unit tests
│   ├── views.py               # API views and business logic
│   ├── management/            # Custom Django management commands
│   │   └── commands/
│   │       └── seed.py        # Database seeding command
│   └── migrations/            # Database migration files
│       ├── __init__.py
│       └── 0001_initial.py    # Initial database schema
└── settings/                  # Additional settings modules
    └── base.py                # Base settings configuration
```

## 🚀 Features

- **Property Listings**: Browse and manage travel property listings
- **Booking System**: Make and manage property bookings
- **Review System**: Leave and view reviews for properties
- **RESTful API**: Django REST Framework powered API
- **Database Seeding**: Custom management commands for sample data
- **Admin Interface**: Django admin for content management

## 🛠️ Models

### Listing Model
- **Fields**: UUID primary key, name, description, location, price_per_night, timestamps
- **Purpose**: Represents travel properties available for booking

### Booking Model
- **Fields**: UUID primary key, property reference, start_date, end_date, total_price, timestamp
- **Purpose**: Manages property reservations

### Review Model
- **Fields**: UUID primary key, property reference, rating (1-5), comment, timestamp
- **Purpose**: User feedback and ratings for properties

## 🔧 Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL (or SQLite for development)
- Virtual environment

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd alx_travel_app
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r alx_travel_app/requirement.txt
   ```

4. **Environment setup**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials and SECRET_KEY
   ```

5. **Database setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Seed database with sample data**
   ```bash
   python manage.py seed
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

## 📊 Database Schema

### Listing Table
```sql
- listings_id (UUID, Primary Key)
- name (VARCHAR(255))
- description (TEXT)
- location (VARCHAR(255))
- price_per_night (DECIMAL(10,2))
- created_at (DATETIME)
- updated_at (DATETIME)
```

### Booking Table
```sql
- booking_id (UUID, Primary Key)
- property_id (UUID, Foreign Key → Listing)
- start_date (DATE)
- end_date (DATE)
- total_price (DECIMAL(10,2))
- created_at (DATETIME)
```

### Review Table
```sql
- review_id (UUID, Primary Key)
- property_id (UUID, Foreign Key → Listing)
- rating (INTEGER, 1-5)
- comment (TEXT)
- created_at (DATETIME)
```

## 🔌 API Endpoints

### Listings
- `GET /api/listings/` - List all listings
- `POST /api/listings/` - Create new listing
- `GET /api/listings/{id}/` - Get specific listing
- `PUT /api/listings/{id}/` - Update listing
- `DELETE /api/listings/{id}/` - Delete listing

### Bookings
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create new booking
- `GET /api/bookings/{id}/` - Get specific booking
- `PUT /api/bookings/{id}/` - Update booking
- `DELETE /api/bookings/{id}/` - Delete booking

### Reviews
- `GET /api/reviews/` - List all reviews
- `POST /api/reviews/` - Create new review
- `GET /api/reviews/{id}/` - Get specific review
- `PUT /api/reviews/{id}/` - Update review
- `DELETE /api/reviews/{id}/` - Delete review

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Run specific app tests:
```bash
python manage.py test listings
```

## 📝 Management Commands

### Seed Database
```bash
python manage.py seed
```
Populates the database with sample listings, bookings, and reviews for development and testing.

## 🔒 Environment Variables

Required environment variables in `.env`:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost:5432/alx_travel_app
```

## 🚀 Deployment

### Production Settings
- Set `DEBUG=False` in environment
- Configure proper database credentials
- Set up static file serving
- Configure ALLOWED_HOSTS

### WSGI/ASGI
- WSGI configuration: `alx_travel_app/wsgi.py`
- ASGI configuration: `alx_travel_app/asgi.py`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- ALX Software Engineering Program

## 🆘 Support

For support and questions, please contact the development team or create an issue in the repository.
