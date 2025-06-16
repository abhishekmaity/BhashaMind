# Build stage
FROM eclipse-temurin:17-jdk as builder
WORKDIR /app
COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./mvnw dependency:go-offline
COPY src ./src
RUN ./mvnw package -DskipTests

# Runtime stage
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
ARG APP_USER=appuser
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
USER $APP_USER
COPY --from=builder /app/target/backend-java-0.0.1-SNAPSHOT.jar ./app.jar
EXPOSE 8080
CMD ["java", "-jar", "app.jar"]
