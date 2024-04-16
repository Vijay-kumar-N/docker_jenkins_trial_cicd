FROM ubuntu:latest
RUN apt update
COPY ./main.go /home/main.go

FROM golang:1.21 AS BUILD
WORKDIR /src
copy --from=0 /home/main.go ./main.go
RUN go build -o /bin/hello ./main.go

FROM scratch
COPY --from=BUILD /bin/hello /bin/hello
CMD [ "/bin/hello" ]
