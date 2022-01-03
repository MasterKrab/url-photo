<script lang="ts">
  import type Screenshot from "../types/screenshot";

  export let promise: Promise<Screenshot> | null;
  export let screenshot: string;
  export let url: string;

  let imageContainer: HTMLDivElement;

  let isFullscreen = false;

  const handleToggleFullscreen = async () => {
    document.fullscreenElement
      ? await document.exitFullscreen()
      : await imageContainer.requestFullscreen();

    isFullscreen = !!document.fullscreenElement;
  };

  const handleFullscreenChange = () => {
    isFullscreen = !!document.fullscreenElement;
  };

  const handleClose = () => (promise = null);
</script>

<svelte:window on:fullscreenchange={handleFullscreenChange} />

<section class="screenshot">
  <h2 class="screenshot__title">Your screenshot is ready!</h2>
  <div class="screenshot__image-container" bind:this={imageContainer}>
    {#if isFullscreen}
      <button
        class="screenshot__close-fullscreen"
        on:click={handleToggleFullscreen}
      >
        <img src="/assets/icons/fullscreen.svg" alt="Exit fullscreen" />
      </button>
    {/if}
    <img
      class="screenshot__image"
      src={screenshot}
      alt="Screenshot from {url}"
    />
  </div>
  <div class="screenshot__buttons">
    <a class="screenshot__button" href={screenshot} download="screenshot"
      >Download</a
    >
    <button class="screenshot__button" on:click={handleToggleFullscreen}
      >Fullscreen</button
    >
    <button class="screenshot__button" on:click={handleClose}
      >Take another screenshot</button
    >
  </div>
</section>

<style lang="scss">
  .screenshot {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1rem;

    @media screen and (min-width: 600px) {
      grid-template-columns: 3fr 1fr;

      &__title {
        grid-column: span 2;
      }
    }

    &__image-container {
      position: relative;
      display: grid;
      place-items: center;
      background-color: var(--primary-color);
    }

    &__close-fullscreen {
      position: absolute;
      top: 15px;
      right: 15px;
      width: 50px;
    }

    &__buttons {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    &__button {
      background-color: var(--element-color);
      padding: 0.75rem 1.25rem;
      font-weight: bold;
      color: var(--primary-color);
    }
  }
</style>
