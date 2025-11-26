create user CoursBDA identified by RCS
default tablespace USERS
temporary tablespace TEMP
profile DEFAULT;
grant connect to CoursBDA;
grant dba to CoursBDA;
grant resource to CoursBDA;
grant unlimited tablespace to CoursBDA;