<template>
  <v-app id="app">
    <div id="nav">
      <router-link to="clientes">Clientes</router-link> |
      <router-link to="categorias">Categorias</router-link>
    </div>
    <router-view/>
  </v-app>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

table > tbody > tr {
  background-color: rgb(165, 165, 166) !important;
}

table {
  background-color: #cccaca !important;
}
</style>
