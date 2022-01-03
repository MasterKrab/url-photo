<script lang="ts">
  import Header from "./components/Header.svelte";
  import Screenshot from "./components/Screenshot.svelte";
  import FlyingFocus from "./components/FlyingFocus.svelte";
  import "./scss/normalize.scss";
  import "./scss/general.scss";
  import "@fontsource/poppins";
</script>

<Header />

<main class="main">
  <Screenshot />
</main>

<FlyingFocus />

<style lang="scss">
  .main {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
    text-align: center;
  }
</style>
