<script setup lang="ts">
const route = useRoute();
const router = useRouter();
</script>

<template>
  <div>
    <Button
      v-if="true"
      @click="router.push('/about')"
    >
      Go to About page
      {{ route.path }}
    </Button>
  </div>
</template>
