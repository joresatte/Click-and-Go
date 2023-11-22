import config from "@/config.js";
import { ref, reactive} from 'vue'

async function getLoginPost (identificatioValue, passwordValue){
    const identify= ref(identificatioValue)
    const pass= ref(passwordValue)
    console.log(identify.value, pass.value)
    const settings = reactive({
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        identification: identify.value,
        password: pass.value
    }),
    })
    const response= ref(null)

    response.value= await fetch(`${config.login_Path}/get_login/Authenticated`, settings)
    console.log(response.value)
    return {response}
            
}
export default getLoginPost