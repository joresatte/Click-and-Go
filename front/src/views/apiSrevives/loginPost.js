import { ref, watchEffect} from 'vue'
import  config from '@/config.js'

export function useFetch(identification, password) {
  const settings = { 
    method: "POST", 
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        identification: identification,
        password: password
    }),
  }
  const data = ref(null)
  const error = ref(null)
  const fetchData = () => {
// reset state before fetching..
data.value = null
error.value = null
const url = ref(`${config.login_Path}/get_login/Authenticated` )
fetch(url, settings)
    .then((res) => res.json())
    .then((json) => (data.value = json))
    .catch((err) => (error.value = err))
  }

  watchEffect(() => {
    fetchData()
  })

  return { data, error }
}