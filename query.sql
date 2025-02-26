SELECT RLLOCD, RLNAME, to_char(sysdate-1,'DD/MM/YYYY')    
FROM AAPEN.STKLOC, AAPEN.RRBRNS WHERE
  (RRROUT = 800 OR RLSPDT > trunc(sysdate)) 
  AND RLCHNL<>'OVERSEAS' AND RLMDEL=0 and rlxml=1
  AND RLLOCD=RRLOCD 
  and not exists (select 1 from AAPEN.storesales where  dadate=trunc(sysdate)-1 and dalocd=rllocd)
  and exists (select 1 from AAPEN.storesales where dalocd=rllocd)
  AND RLLOCD NOT IN (57
129
130
149
150
162
168
188
196
203
222
235
240
241
245
255
261
274
275
281
288
292
295
300
303
315
318
319
325
340
70
116
126
138
146
177
186
202
204
214
216
223
238
252
253
262
311
62
71
72
80
83
97
114
154
163
164
165
175
179
181
217
224
227
277
296
310
323
337
338
88
98
117
127
134
171
173
273
284
287
63
67
85
166
176
234
244
302
317
322
324
79
89
99
124
141
159
178
183
212
218
256
258
267
282
301
313
327
339
151
213
266
270
276
285
309
314
320
946
948
77
112
133
156
205
293
308
312
329

)
  ORDER BY RLLOCD;