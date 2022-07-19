int correct_tail(const char *body, const char *tail) {
  if (strlen(tail) <= strlen(body))
    return ((body[strlen(body) - 1] == tail[0]) ? 1 : 0 );
}
