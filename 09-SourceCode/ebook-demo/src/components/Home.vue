<template>
  <div class="hello">
    <h1>hello, world</h1>
    <router-link to="/ebook?user_id=1&book_id=2">
      <button class="button1" type="primary">点击回家</button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  methods: {
    tiaoZhuan() {
      this.$router.push('/ebook')
      this.$message({
        showClose: true,
        message: 'Welcome',
        type: 'success'
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
