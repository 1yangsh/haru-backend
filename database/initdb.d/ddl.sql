create table if not exists dog
(
    birthday date                    null,
    weight   double                  null,
    name     varchar(5)              null,
    dog_id   bigint auto_increment
        primary key,
    home_id  varchar(255)            null,
    img_url  varchar(255)            null,
    gender   enum ('MALE', 'FEMALE') null,
    constraint UK_irtty3r4wtderqppcc902sto
        unique (home_id)
);

create table if not exists home
(
    dog_id    bigint       null,
    home_id   varchar(255) not null
        primary key,
    home_name varchar(255) null,
    constraint UK_s7wdp93s1q2k3xipsj7g8lv42
        unique (dog_id),
    constraint FK2xh072y6kptbxa5x2h4f4p08i
        foreign key (dog_id) references dog (dog_id)
);

alter table dog
    add constraint FKa6sbkuuwt11l18ywr2iu9xrwj
        foreign key (home_id) references home (home_id);

create table if not exists schedules
(
    is_active         bit                                                                                        not null,
    is_deleted        bit                                                                                        null,
    created_date      datetime(6)                                                                                null,
    modified_date     datetime(6)                                                                                null,
    schedule_datetime datetime(6)                                                                                not null,
    schedule_id       bigint auto_increment
        primary key,
    home_id           varchar(255)                                                                               not null,
    memo              text                                                                                       null,
    repeat_id         varchar(255)                                                                               null,
    alert_type        enum ('NONE', 'ON_TIME', 'FIVE_MINUTES', 'THIRTY_MINUTES', 'ONE_HOUR')                     null,
    repeat_type       enum ('NONE', 'DAY', 'WEEK', 'MONTH', 'YEAR')                                              null,
    schedule_type     enum ('WALK', 'WASH', 'POO', 'BRUSH', 'FOOD', 'GROOM', 'HOSPITAL', 'WATER', 'ANNIVERSARY') not null
);

create table if not exists users
(
    allow_notification tinyint(1)                                                        null,
    is_deleted         tinyint(1)                                                        null,
    dog_id             bigint                                                            null,
    user_id            bigint auto_increment
        primary key,
    email              varchar(255)                                                      null,
    home_id            varchar(255)                                                      null,
    img_url            varchar(255)                                                      null,
    nickname           varchar(255)                                                      null,
    user_role          enum ('DAD', 'MOM', 'UNNIE', 'OPPA', 'NUNA', 'HYEONG', 'YOUNGER') null,
    constraint UK_6dotkott2kjsp8vw4d0m25fb7
        unique (email),
    constraint FK1ddu6xk8qjg6v4lcrcctn3ec0
        foreign key (home_id) references home (home_id),
    constraint FKh5nem1ia0w3pggn6x08rj5b6x
        foreign key (dog_id) references dog (dog_id)
);

create table if not exists activity_logs
(
    created_date  datetime(6)                                                                                null,
    id            bigint auto_increment
        primary key,
    user_id       bigint                                                                                     null,
    home_id       varchar(255)                                                                               null,
    schedule_type enum ('WALK', 'WASH', 'POO', 'BRUSH', 'FOOD', 'GROOM', 'HOSPITAL', 'WATER', 'ANNIVERSARY') not null,
    constraint FK5bm1lt4f4eevt8lv2517soakd
        foreign key (user_id) references users (user_id),
    constraint FKqhcmf6rj8nw4srowdfxb65mgm
        foreign key (home_id) references home (home_id)
);

create table if not exists notifications
(
    notification_id   bigint auto_increment
        primary key,
    send_date         datetime(6)                 null,
    user_id           bigint                      null,
    message           varchar(255)                null,
    notification_type enum ('SCHEDULE', 'SYSTEM') not null,
    constraint FK9y21adhxn0ayjhfocscqox7bh
        foreign key (user_id) references users (user_id)
);

create table if not exists user_schedules
(
    schedule_id bigint not null,
    user_id     bigint not null,
    primary key (schedule_id, user_id),
    constraint FK8pafog8r9r153mv7f2n0pm8ah
        foreign key (schedule_id) references schedules (schedule_id),
    constraint FKqiwy3sdspgnrcj1lkq3jor4k3
        foreign key (user_id) references users (user_id)
);

create table if not exists schedules_mates
(
    mates_schedule_id    bigint not null,
    mates_user_id        bigint not null,
    schedule_schedule_id bigint not null,
    constraint UK_k5bfirc9nt516m1j97l5ojfvj
        unique (mates_schedule_id, mates_user_id),
    constraint FKn62x9dp60y6jvrasgpo9th7a9
        foreign key (mates_schedule_id, mates_user_id) references user_schedules (schedule_id, user_id),
    constraint FKpbnw8wak8vt4njghyntewx7hv
        foreign key (schedule_schedule_id) references schedules (schedule_id)
);

