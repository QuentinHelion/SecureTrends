# SecureTrends - Cyber Threat Intelligence

## Principle
Discover our cyber-focused technological intelligence API! Powered by RSS feeds from leading cyber news sites, this API keeps you constantly informed about the latest advancements and emerging threats in the field of cybersecurity.

With this technological intelligence API, you can easily integrate cyber news RSS feeds into your own applications, monitoring systems, or customized dashboards. In real-time, you receive updates on new vulnerabilities, ongoing attacks, cybersecurity trends, and best practices to safeguard your data.

## Installation
This application runs using docker to allow a wide range of compatibility

#### Requirements
```
docker
docker-compose
```

#### Installation
```
# Classic run (blocking run)
docker-compose up

# To run app in background add -d option
docker-compose up -d
```

When server is started, you can run a first scan of all platform like this
```
http://myapp:5000/rss
```

## Usage

To get feed, use this route
```
http://myapp:5000/feed
```
#### Custom research 

Explication:
You can custom your research with 2 parameter: **platform** and **interval**.
- Platform correspond to title of website / platform, permit to get feed of specified source
- Interval correspond to the age of the feed since today (in day)

Example:
- Platform: ``http://myapp:5000/feed?platform=CISA`` 
- Interval: ``http://myapp:5000/feed?interval=3`` *(parameter is number of day)*
- Cumulative: ``http://myapp:5000/feed?interval=3&platform=CISA``

## Configuration

#### Add Threat Intelligence platform
In file ``platforms.json`` you can simple add new aray with basic informations:
- name: name of website/platform 
- url: **RSS url** of website/platform 

Example:
```
{
  "name": "WebSite",
  "url": "https://website.com/rss"
}
```
