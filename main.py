import OID
import UI
import FileHandlers as FH
import Messager as M

UI.Beep()
print("Camera started")
if UI.Query_Config("email - ") is None:
    email = input("\u001b[35mPlease enter an email: ")  # Needs try catch
    FH.Update_Config("email - " + email)
    M.Hello()
else:
    print("\u001b[35mWe will use[", UI.Query_Config("email - "), "]as the user email")
try:
    OID.Process(camera=0)
except:
    FH.Update_Log("OID error")
    print("\u001b[36mCould not open camera. If you can't fix this issue. Please email us at printeye2021@gmail.com")
