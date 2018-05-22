#include <Python.h>
/* Python.h already include those two: */
/* #include <stdio.h> */
/* #include <stdlib.h> */
#include <security/pam_appl.h>
#include <security/pam_modules.h>


PAM_EXTERN int
pam_sm_authenticate(pam_handle_t *pamh, int flags, int argc, const char **argv)
{
        PyObject *lockatme;
        lockatme = PyImport_Import(Py_BuildValue("s", "lockatme"));


        Py_Initialize();
        return PAM_SUCCESS;
}

PAM_EXTERN int
pam_sm_acct_mgmt(pam_handle_t *pamh, int flags, int argc, const char **argv)
{
        return PAM_SERVICE_ERR;
}

PAM_EXTERN int
pam_sm_setcred(pam_handle_t *pamh, int flags, int argc, const char **argv)
{
        return PAM_SERVICE_ERR;
}

PAM_EXTERN int
pam_sm_chauthtok(pam_handle_t *pamh, int flags, int argc, const char **argv)
{
        return PAM_SERVICE_ERR;
}

PAM_EXTERN int
pam_sm_open_session(pam_handle_t *pamh, int flags, int argc, const char **argv)
{
        return PAM_SERVICE_ERR;
}
PAM_EXTERN int
pam_sm_close_session(pam_handle_t *pamh, int flags, int argc, const char **argv)
{
        return PAM_SERVICE_ERR;
}
