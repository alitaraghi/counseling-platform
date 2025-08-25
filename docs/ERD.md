# Entity-Relationship Diagram (ERD)

## Entities
### User
- id (PK)
- email (Unique)
- password (Hashed)
- role (Choices: Counselor/Client/Admin)
- created_at (DateTime)
- updated_at (DateTime)
- is_staff (Boolean, for admin access)
- is_superuser (Boolean, for super admin)

### CounselorProfile
- user_id (FK, One-to-One with User)
- license_number (String)
- license_doc (FileField, for verification)
- specialty (String, e.g., "Depression", "Anxiety")
- bio (Text)
- verified (Boolean, for Iran/Australia compliance)

### ClientProfile
- user_id (FK, One-to-One with User)
- full_name (String, Encrypted)
- birth_date (Date, Encrypted)
- contact_info (Text, Encrypted)

### BlogPost
- id (PK)
- counselor_id (FK to User where role='Counselor')
- title (String)
- content (Text)
- video_url (URL, Nullable)
- is_public (Boolean)
- created_at (DateTime)

### Course
- id (PK)
- counselor_id (FK to User where role='Counselor')
- title (String)
- description (Text)
- created_at (DateTime)

### CourseContent
- id (PK)
- course_id (FK)
- type (Choices: Video/Text/Quiz)
- content (Text or File)
- order (Integer)

### ClientCourseProgress
- client_id (FK to User where role='Client')
- course_id (FK)
- progress (Float, 0-100)
- badges (JSON, e.g., ["Completed Module 1"])

### ClientFile
- id (PK)
- client_id (FK to User where role='Client')
- counselor_id (FK to User where role='Counselor')
- summary (Text, Encrypted)
- diagnoses (JSON, Encrypted)
- created_at (DateTime)

### Session
- id (PK)
- counselor_id (FK to User where role='Counselor')
- client_id (FK to User where role='Client')
- date_time (DateTime)
- status (Choices: Scheduled/Completed/Canceled)
- payment_status (Choices: Paid/Pending/Refunded)
- ai_summary (Text, Encrypted, Nullable)

### Payment
- id (PK)
- client_id (FK to User where role='Client')
- session_id (FK, Nullable)
- course_id (FK, Nullable)
- amount (Decimal)
- status (Choices: Completed/Pending/Failed)
- created_at (DateTime)

### AITriage
- id (PK)
- user_id (FK to User)
- symptoms (JSON)
- suggestions (Text)
- created_at (DateTime)

### ForumPost
- id (PK)
- user_id (FK to User)
- content (Text)
- is_moderated (Boolean)
- created_at (DateTime)

### Consent
- id (PK)
- user_id (FK to User)
- session_id (FK, Nullable)
- course_id (FK, Nullable)
- agreed_at (DateTime)
- details (Text, e.g., "Consent for session recording")

## Relationships
- User → CounselorProfile/ClientProfile: One-to-One
- User (role='Counselor') → BlogPost/Course/Session: One-to-Many
- User (role='Client') → ClientFile/Session/ClientCourseProgress: One-to-Many
- Course → CourseContent: One-to-Many
- User (role='Client') + Course → ClientCourseProgress: Many-to-Many
- Session → Payment: One-to-One
- User → Consent: One-to-Many

## Legal Considerations
- Encrypted fields (e.g., summary, contact_info) for Iran/Australia privacy laws.
- verified field in CounselorProfile for license checks (Iran: Medical Council; Australia: AHPRA).
- Consent table for explicit user agreement (Privacy Act 1988, Australia).
- Soft delete (is_deleted field, not shown) for data removal requests.