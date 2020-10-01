<script>
	import { getRandomNumber } from '../utils/webEndpoints.js';
	let randPromise = getRandomNumber();
</script>

<main>
	<h1>Home Page!!!</h1>
	{#await randPromise}
	<p>Generating random number</p>
	{:then randNumber}
	<p>Your random number is {randNumber}</p>
	{:catch}
	<p>A random number could not be found.</p>
	{/await}
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>