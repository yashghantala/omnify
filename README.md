# Event Management System

Headless event management system to manage events and its attendees.

## Prerequisites

```bash
Git
Python 3.12
```

## Installation (Local)

Clone repository
```bash
git clone https://github.com/yashghantala/omnify.git
```

Install dependencies by running command below in project root directory
```bash
pip install -r ./requirement.txt
```

Run server
```bash
python manage.py runserver
```

Create admin account required for other user creation
```bash
python manage.py createsuperuser
```

Use provided credentials to login into admin panel and add users as needed

## API Reference
#### Common header requirement for authentication
Include below header in all requests except for login one
```http
Authorization: Token <token>
```

#### Get authentication token

```http
  POST /api/authenticate/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | - |
| `password` | `string` | - |

Returns `token` which you'll need to pass in request header

#### Create event

```http
  POST /api/events/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `name` | `string` | `Event name` |
| `location` | `string` | `Place of event` |
| `start_time` | `date time` | `Start time of a event (format yyyy-MM-ddTHH:mm:ssZ)` |
| `end_time` | `date time` | `End time of a event (format yyyy-MM-ddTHH:mm:ssZ)` |
| `max_capacity` | `number` | `Total attendees event can have` |

Returns HTTP 201 on success

#### Get all events

```http
  GET /api/events/
```
Returns all the upcoming events

#### Register attendee

```http
  POST /api/events/{event_id}/register
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{event_id}` | `number` | `ID of an event` |
| `name` | `string` | `Name of attendee` |
| `email` | `string` | `Email of attendee` |

Returns HTTP 201 on success

#### Get event attendees

```http
  GET /api/events/{event_id}/attendees/?<next_page>  
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `{event_id}` | `number` | `ID of an event` |
| `<next_page>` | `number` | **(Optional)** `next page hash received with previous page load` |

Response
| Key | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `results` | `json` | `List of attendees` |
| `next` | `string` | `Link to next page` |

Returns event attendees page by page

## Sample test requests

check `thunder-collection_postman_Omnify.json` for sample requests
