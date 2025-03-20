# Build stage
FROM node:20-alpine AS build-stage

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm install
COPY . /app
RUN npm run build

# Production stage (servidor estático com Nginx)
FROM nginx:1.25-alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80
