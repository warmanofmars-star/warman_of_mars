with open ("greeting.txt", "w", encoding = "utf-8") as file:
    file.write("Hello, automated tests! \n")
    file.write("Second line")

#file = open (...)
#file.close ()
#"r" - read
#"w" - write (rewrite)
#"a" - append
#"r+" - read and write
#"rb", "wb" - pdf, screenshots


def log_test_result (test_name, status):
    with open("test_run.log", "a", encoding="utf-8") as log_file:
        log_file.write(f"{test_name}:{status}\n")

log_test_result("test login", "PASSED")
log_test_result("test registration", "FAILED")
log_test_result("test logout", "PASSED")