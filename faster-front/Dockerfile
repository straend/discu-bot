FROM node:alpine AS builder
WORKDIR /app

COPY package.json .
RUN npm install --legacy-peer-deps

COPY . .
ARG CHANNEL_API_URL
RUN npm run build --prod

FROM nginx:alpine

COPY --from=builder /app/dist/faster-front/* /usr/share/nginx/html/
COPY nginx.conf /etc/nginx/conf.d/default.conf