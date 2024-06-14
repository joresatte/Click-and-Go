import { ref, toValue } from 'vue'
import { defineStore } from 'pinia'
import { useRouter, useRoute } from 'vue-router'
export const usePiniaStore = defineStore('Store', () => {
  const showTemplate = ref(false)
  const router = useRouter()
  const route = useRoute()
  const data = ref(null)
  const error = ref(null)
  const fetching = ref(true)
  const response = ref()
  const resError = ref()
  const pathId = ref(null)
  const customerStatus = ref(null)
  const getIdentity = () => {
    if (window.localStorage) {
      if (
        localStorage.getItem('dataIdentity') !== undefined &&
        localStorage.getItem('dataIdentity')
      ) {
        // piniaStore.showModal= false
        return true
      } else {
        return false
      }
    }
  }

  const getData = async (url, options) => {
    try {
      let res = await fetch(toValue(url), options)
      data.value = res
    } catch (errors) {
      error.value = errors
      console.log(error.value)
    } finally {
      fetching.value = false
    }
  }

  return {
    router,
    showTemplate,
    route,
    data,
    error,
    resError,
    response,
    fetching,
    pathId,
    customerStatus,
    getIdentity,
    getData
  }
})
