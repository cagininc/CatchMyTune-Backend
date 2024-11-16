# Catch My Tune 🎶

**Catch My Tune** – An intelligent audio analysis platform designed to provide in-depth insights into music tracks using the power of the **Spotify API** and **Librosa**. This backend-focused project is built to offer endpoints for analyzing tempo, key, and other audio features, making it ideal for developers, music analysts, and hobbyist musicians looking for data-rich insights.**Songs are processed asynchronously to extract features such as tempo and key**. **Celery **is used for background task execution to ensure the upload process is smooth for the user, while **Redis **acts as a message broker for managing Celery tasks efficiently. This architecture allows the analysis to run seamlessly in the background, improving user experience by avoiding long wait times.

## Tech Stack

- **Python** & **Django** – Backend framework for scalable API management.
- **Spotify API** – For track metadata and real-time music analysis.
- **Librosa** – Advanced audio analysis, including tempo, pitch, and spectral features.
- **PostgreSQL** – Database for efficient, scalable data storage.
- **Supabase** (PostgreSQL as a Service) – Cloud database hosting for high availability.
- **Docker** *(planned)* – For containerized deployment.
- **CI/CD** with **GitHub Actions** *(planned)* – Ensures seamless updates and testing.
- **Redis**
- **Celery**
## Screenshots
![Catch-My-Tune-Frontend](/ui-test.png)
## Vision

Create a sophisticated tool for music enthusiasts and developers, bridging technology with audio analysis to unlock insights into any track's musical DNA.

---

This project is still in development; stay tuned for updates! 🚀
