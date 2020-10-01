<script>
  import router from "page";
  import Home from "./pages/Home.svelte";
  import About from "./pages/About.svelte";
  let page;

  router("/", () => (page = Home));
  router("/about", () => (page = About));

  router.start();
</script>

<style>

</style>

<main>
  <nav>
	<a href="/">Home</a>
	<a href="/about">About</a>
  </nav>
  <svelte:component this={page} />
</main>
