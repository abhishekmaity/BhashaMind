# Build stage
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
# Ensure dependencies are installed first for better layer caching
RUN npm install
COPY . .
RUN npm run build

# Production stage
FROM nginx:stable-alpine
WORKDIR /app
# WORKDIR is not strictly necessary for Nginx serving static files but good practice
ARG APP_USER=appuser
# Create a non-root user and group
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER

# Copy built assets from the builder stage
COPY --from=builder /app/build /usr/share/nginx/html

# Optional: Add custom nginx configuration if needed
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Switch to the non-root user
USER $APP_USER

# Nginx listens on port 80 by default
EXPOSE 80
# The base nginx image handles starting nginx. CMD can be removed.
# CMD ["nginx", "-g", "daemon off;"]
