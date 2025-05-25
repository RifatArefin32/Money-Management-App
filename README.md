# Money Management App
## Project Setup
- Clone the project
- Create virtual environment and activate it
- Install packages of `requirements.txt` file in your virtual environment
- After using usage, must deactivate the virtual environment


## Database Configuration
- Database type: PostgreSQL
- Database name: money_management_app_db
- Database user: money_management_app_user
- Database password: password
  
## Add fake data
Run the following commands after configuring databases.
```bash
python manage.py dummy_core_data    # Create core data
```