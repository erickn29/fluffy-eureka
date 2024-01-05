<template>
    <div v-if="vacancy">
        <h1>{{ vacancy.title }}</h1>

       {{ vacancy.salary_from}} - {{ vacancy.salary_to }}
    </div>
    <div v-else>
        404
    </div>
</template>

<script setup>
    const { id } = useRoute().params

    definePageMeta (
        {
            layout: 'post',
        }
    )
        
    const { data: vacancy } = await useFetch(
        'http://127.0.0.1:8000/api/v1/vacancy/' + id + '/'
        )

</script>