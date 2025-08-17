FROM python
WORKDIR /app
COPY . /app
CMD ["make", "boot_container"]