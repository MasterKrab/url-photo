<script lang="ts">
  import Form from "../components/Form.svelte";
  import ScreenshotResult from "../components/ScreenshotResult.svelte";
  import Spinner from "../components/Spinner.svelte";
  import LoadingText from "../components/LoadingText.svelte";
  import type Screenshot from "../types/screenshot";

  let screenshotPromise: Promise<Screenshot> | null;

  const handleSubmit = async ({ detail }: CustomEvent) => {
    const { url } = detail;

    const queryParams = Object.entries(detail)
      .map(([key, value]) => `${key}=${value}`)
      .join("&");

    screenshotPromise = fetch(`/api/screenshot?${queryParams}`).then(
      async (response) => ({
        url,
        ...(await response.json()),
      })
    );
  };
</script>

<h1 class="title">URL Photo 📷</h1>
<p class="text">
  The <span class="text__highlight">easiest</span> way to take a
  <span class="text__highlight">screenshot</span> of a website.
</p>

{#if screenshotPromise}
  {#await screenshotPromise}
    <div class="loading">
      <LoadingText text="Your screenshot is loading..." />
      <Spinner />
    </div>
  {:then screenshot}
    <ScreenshotResult bind:promise={screenshotPromise} {...screenshot} />
  {:catch}
    <Form on:submit={handleSubmit} />
    <p class="error">An error ocurred, try again later.</p>
  {/await}
{:else}
  <Form on:submit={handleSubmit} />
{/if}

<style lang="scss">
  .title {
    font-size: min(8vw, 3rem);
  }

  .text {
    font-size: min(6vw, 1.8rem);

    &__highlight {
      font-weight: bold;
      color: var(--element-color);
    }
  }

  .loading {
    margin-top: 8rem;
  }

  .error {
    color: var(--danger-color);
    font-size: 1.25rem;
  }
</style>
