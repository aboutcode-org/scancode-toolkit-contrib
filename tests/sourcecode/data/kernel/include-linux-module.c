#endif
#include <linux/version.h>
#include <linux/config.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/skbuff.h>
#define	DPRINTF(sc, _fmt, ...) do {					\
	if (sc->sc_debug & 0x10)					\
		printk(_fmt, __VA_ARGS__);				\
} while (0)
#else
